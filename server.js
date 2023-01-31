const express = require("express");
const child_process = require("child_process");
const path = require("path");
const app = express();

app.use(express.static("public"))

function streamToString (stream) {
    const chunks = [];
    return new Promise((resolve, reject) => {
      stream.on('data', (chunk) => {
        // console.log(chunk.toString());
        chunks.push(Buffer.from(chunk))
      });
      stream.on('error', (err) => reject(err));
      stream.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    })
}

app.get("/:type", async (req, res, next) => {
    const type = req.params.type;
    if (type != "classroom" && type != "lab") {
        return next()
    }
    const day = req.query.day?.toLocaleLowerCase();
    const timeslot = req.query.timeslot?.toLocaleLowerCase();
    const classroom = req.query.classroom;

    let script_path;
    if (type == "classroom") {
        script_path = path.resolve(`./scripts/${day}/${day}_cr.py`);
    } else if (type == "lab") {
        script_path = path.resolve(`./scripts/${day}/${day}_lab.py`);
    }
    const child = child_process.spawn("python", [script_path], { cwd: path.resolve(`./scripts/${day}`) });

    child.on("close", (code) => {
        if (code != 0) {
            console.log("Error");
        }
    })

    child.on("error", (err) => {
        console.log(err);
    })

    if (timeslot != null) {
        child.stdin.write("a\n");
        child.stdin.write(`${timeslot.toLocaleLowerCase()}\n`);
    } else if (classroom != null) {
        child.stdin.write("b\n");
        child.stdin.write(`${classroom}\n`);
    } else {
        return res.json({
            availability: ["Timeslot or classroom is required"]
        })
    }
    child.stdin.end();
    
    const output = (await streamToString(child.stdout)).split(/[\n\r]+/).filter((element) => {
        if (element == "") return false;
        return true;
    })
    if (output.length == 0) {
        output.push("Not available")
    }
    return res.json({ availability: output });
})

app.listen(3000, () => { console.log("Listening on port 3000"); });
const app1 = require("express") ();
const PORT =  process.env.PORT;
var temp = process.pid;
var processid = '' + temp;

if (!PORT) {
    throw new Error ("PORT variable not defined");
}

app1.get("/",(req,res) => {
    const data = `app-id: ${processid}, running at PORT ${PORT}`;
    return res.send(data);
});
app1.listen(PORT, ()=>console.log(process.pid, ` is listening on ${PORT}`));

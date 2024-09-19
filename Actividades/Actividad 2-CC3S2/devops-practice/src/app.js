const express = require("express")

const app = express();

app.get('/:name',(req,res) => {
    res.send(`Hello ${req.params.name}`);
})

module.exports = app;

if(require.main === module){
    const port = process.env.PORT || 3000;
    
    app.listen(port,()=> {
        console.log(`Server running on port ${port}`);
    })
}
import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props){
    super(props)
    this.state={
      input:{"text":'ここに検索文字を入力'},
      output:{
        "score":'',
        "kaiseki_naiyou":''
      },
    }
    this.onChangeHander = this.onChangeHander.bind(this)
    this.submitHandle = this.submitHandle.bind(this)
  }
  onChangeHander(e){
    this.setState({input:{text:e.target.value}});
    console.log(this.state.input.text);
  }
  async submitHandle(){
    const url = 'http://localhost:5000/api'
    //console.log(this.state)
    const res = await fetch(url,{
      method: 'POST',
      mode: 'cors',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body:JSON.stringify(this.state.input),
    })
    console.log(res);
    
    res.json().then(message_json => {
      //console.log(message_json);
      const out_msg=message_json["out"];
      console.log(out_msg["kanjou"]);
      this.setState({output:{
        "score":out_msg["kanjou"],
        "kaiseki_naiyou":out_msg["kaisekibun"],
      }})
    })
  }

  render() {
    return (
      <div className="App">
        <h1>テキストの感情の度合いを図ります</h1>
        <div>
          <input value={this.state.input.text} onChange={this.onChangeHander}type="text"/>
          <button onClick={this.submitHandle} type="submit">判定！</button>
        </div>
        <p>感情の点数：{this.state.output.score}</p>
        <div>
          {this.state.output.kaiseki_naiyou.split("\n").map(m => (<p>{m}</p>))}
        </div>
      </div>
    );
  }
}
export default App;

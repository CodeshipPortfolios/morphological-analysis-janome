import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props){
    super(props)
    this.state={
      text:'特定サイトの検索順位を上げる為に微妙な医療情報をネットに流布する行為は問題と考えまして十ヶ月ぶりにブログを書きました。',
    }
    this.onChangeHander = this.onChangeHander.bind(this)
    this.submitHandle = this.submitHandle.bind(this)
  }
  onChangeHander(e){
    this.setState({text:e.target.value});
    console.log(this.state.text);
    
  }
  submitHandle(){
    const url = 'http://localhost:5000/api'
    console.log(this.state)
    fetch(url,{
      headers:{'Access-Control-Allow-Origin':'*'},
      method: 'POST',
      mode: 'cors',
      data: this.state
    }).then(response => {
      return response.text();
    })
  }
  render() {
    return (
      <div className="App">
        <p>テキストの感情の度合いを図ります</p>
        <input value={this.state.text} onChange={this.onChangeHander}type="text"/>
        <button onClick={this.submitHandle} type="submit">判定！</button>
      </div>
    );
  }
}

export default App;

import React, { Component } from "react";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Home from "./Home";
import Form from "./Form";

class Main extends Component {
  render() {
    return (
        <HashRouter>
                <div>
                  <h1>Soil Stabilizer</h1>
                  <ul className="header">
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/form">Form</NavLink></li>
                  </ul>
                  <div className="content">
                    <Route exact path="/" component={Home}/>
                    <Route path="/form" component={Form}/>
                  </div>
                </div>
        </HashRouter>
    );
  }
}

export default Main;
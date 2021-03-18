import React, { Component } from "react";
import "./main.css";

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
      <div className="header">
        <HashRouter>
                <div>
                  <div className="title">
                    <h1>Soil Stabilizer</h1>
                  </div>
                  <ul>
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/form">Form</NavLink></li>
                  </ul>
                  <div className="content">
                    <Route exact path="/" component={Home}/>
                    <Route path="/form" component={Form}/>
                  </div>
                </div>
        </HashRouter>
        <body className="website-page">
        </body>
      </div>
    );
  }
}

export default Main;
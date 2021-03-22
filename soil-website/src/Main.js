import React, { Component } from "react";
import "./main.css";

import {
    Route,
    NavLink,
    HashRouter
} from "react-router-dom";
import Home from "./Home";
import Form from "./Form";
import Admin from "./Admin";

class Main extends Component {
    render() {
        return (
            <div>
                <HashRouter>
                    <div>
                        <div className="title">
                            <h1>Soil Stabilizer Computation Tool</h1>
                        </div>
                        <div className="textstyle">
                            <NavLink to="/">Home</NavLink>
                        </div>
                        <div className="textstyle">
                            <NavLink to="/form">Form</NavLink>
                        </div>
                        <div className="textstyle">
                            <NavLink to="/admin">Admin</NavLink>
                        </div>
                        <div className="content">
                            <Route exact path="/" component={Home} />
                            <Route path="/form" component={Form} />
                            <Route path="/admin" component={Admin} />
                        </div>
                    </div>
                </HashRouter>
            </div>
        );
    }
}

export default Main;
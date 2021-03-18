import React, { Component } from "react";
import ExcelReader from './ExcelReader';
import "./form.css"

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            dataFile: [],
            liquidLimit: 0,
            plasticIndex: 0,
            clayPercent: 0,
            siltPercent: 0,
            sandPercent: 0,
            organicContent: 0,
            limeCementStabilize: false,
            limeCementDose: false,
            quantResult: false,
            qualResult: false
        }
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;

        this.setState({
            [name]: value
        });
    }


    handleSubmit(event) {
        console.log(JSON.stringify(this.state, null, 2));
    }

    render() {
        return (
            <div className="center-border">
              <div className="margin">
                <ExcelReader/>
                <br />
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Liquid Limit:&nbsp;
                        <input
                            name="liquidLimit"
                            type="number"
                            value={this.state.liquidLimit}
                            max="3"
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label>
                        Plasticity Index:&nbsp;
                        <input
                            name="plasticIndex"
                            type="number"
                            value={this.state.plasticIndex}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label>
                        Clay Percentage:&nbsp;
                        <input
                            name="clayPercent"
                            type="number"
                            value={this.state.clayPercent}
                            max="100"
                            onChange={this.handleInputChange} />
                    </label>&nbsp;%
                    <br />
                    <label>
                        Silt Percentage:&nbsp;
                        <input
                            name="siltPercent"
                            type="number"
                            value={this.state.siltPercent}
                            max="100"
                            onChange={this.handleInputChange} />
                    </label>&nbsp;%
                    <br />
                    <label>
                        Sand Percentage:&nbsp;
                        <input
                            name="sandPercent"
                            type="number"
                            value={this.state.sandPercent}
                            max="100"
                            onChange={this.handleInputChange} />
                    </label>&nbsp;%
                    <br />
                    <label>
                        Organic Content:&nbsp;
                        <input
                            name="organicContent"
                            type="number"
                            value={this.state.organicContent}
                            max="100"
                            onChange={this.handleInputChange} />
                    </label>&nbsp;%
                    <br />
                    <h2>Result Types</h2>
                    <label> Lime or Cement Stabilization
                        <input
                            name="limeCementStabilize"
                            type="checkbox"
                            checked={this.state.limeCementStabilize}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label> Dose of Lime or Cement
                        <input
                            name="limeCementDose"
                            type="checkbox"
                            checked={this.state.limeCementDose}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label> Quantitative Result
                        <input
                            name="quantResult"
                            type="checkbox"
                            checked={this.state.quantResult}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label> Qualitative Result
                        <input
                            name="qualResult"
                            type="checkbox"
                            checked={this.state.qualResult}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <input type="submit" value="Submit" />
                </form>
              </div>
            </div>
        )
    }
};

export default Form;

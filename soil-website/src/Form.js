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
        // TODO: Get correct path for dev/prod on fetch requests.
        fetch('http://localhost:8000/report/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/pdf'
            }
        })
            .then(res => res.blob())
            .then(blob => {
                var file = window.URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = file;
                a.download = 'Soil_Stabilizer_Report.pdf';
                document.body.appendChild(a);
                a.click();
                setTimeout(() => {
                    a.remove();
                    window.URL.revokeObjectURL(file);
                }, 1000)
            });
    }

    render() {
        return (
            <div className="center-border">
              <div className="margin">
                <div className="centered">
                    <p> Choose to either upload a file <strong>OR</strong> manually enter inputs.</p>
                </div>
                <form onSubmit={this.handleSubmit}>
                    <div className="row">

                        <div className="column">
                            <ExcelReader/>
                        </div>
                        <div className="column">
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
                    </div>
                </div>
                <span>
                    <h2>Result Types</h2>
                    <label> Cement Stabilization
                        <input
                            name="cementStabilize"
                            type="checkbox"
                            checked={this.state.limeCementStabilize}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label> Dose of Cement
                        <input
                            name="cementDose"
                            type="checkbox"
                            checked={this.state.limeCementDose}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label> Lime Stabilization
                        <input
                            name="limeCementStabilize"
                            type="checkbox"
                            checked={this.state.limeStabilize}
                            onChange={this.handleInputChange} />
                    </label>
                    <br />
                    <label> Dose of Lime
                        <input
                            name="limeCementDose"
                            type="checkbox"
                            checked={this.state.limeDose}
                            onChange={this.handleInputChange} />
                    </label>
                        <br />
                        <label>
                            Sand Percentage:&nbsp;
                        <input
                                name="sandPercent"
                                type="number"
                                value={this.state.sandPercent}
                                max="100"
                                onChange={this.handleInputChange} />
                            &nbsp;%
                    </label>
                        <br />
                        <label>
                            Organic Content:&nbsp;
                        <input
                                name="organicContent"
                                type="number"
                                value={this.state.organicContent}
                                max="100"
                                onChange={this.handleInputChange} />
                            &nbsp;%
                    </label>
                    <br />
                    <br />
                <input type="submit" value="Submit" />
              </span>
            </form>
            </div>

            </div>
        )
    }
};

export default Form;

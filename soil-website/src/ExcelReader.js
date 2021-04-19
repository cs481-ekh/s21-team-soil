import React, { Component } from 'react';
import XLSX from 'xlsx';
import { make_cols } from './MakeColumns';
import { SheetJSFT } from './types';
import Form from './Form';

class ExcelReader extends Component {
  constructor(props) {
    super(props);
    this.state = {
      file: {},
      data: [],
      cols: []
    }
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    const files = e.target.files;
      if (files && files[0]) {
          this.setState({ file: files[0] }, () => {
              const reader = new FileReader();
              const rABS = !!reader.readAsBinaryString;

              reader.onload = (e) => {
                  /* Parse data */
                  const bstr = e.target.result;
                  const wb = XLSX.read(bstr, { type: rABS ? 'binary' : 'array', bookVBA: true });
                  /* Get first worksheet */
                  const wsname = wb.SheetNames[0];
                  const ws = wb.Sheets[wsname];
                  const data = XLSX.utils.sheet_to_json(ws);
                  this.setState({ data: data, cols: make_cols(ws['!ref']) }, () => {

                      this.props.handleFile(this.state.data);

                  });

              };

              if (rABS) {
                  reader.readAsBinaryString(this.state.file);
              } else {
                  reader.readAsArrayBuffer(this.state.file);
              };
          });
      }
  };

  render() {
    return (
      <div>
        <label htmlFor="file">Choose an Excel File</label>
        <br />
            <input type="file" className="form-control" id="file" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" onChange={this.handleChange} />
        <br />
      </div>

    )
  }
}

export default ExcelReader;
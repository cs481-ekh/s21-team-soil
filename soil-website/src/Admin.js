import React, { Component } from "react";
import DataTable from 'react-data-table-component';

class Admin extends Component {

    UserData = [];
    Columns = [
        {
            name: 'First Name',
            selector: (row) => row['first_name'],
            sortable: true
        },
        {
            name: 'Last Name',
            selector: (row) => row['last_name'],
            sortable: true
        },
        {
            name: 'Email',
            selector: (row) => row['email'],
            sortable: true
        },
        {
            name: 'Last Accessed',
            selector: (row) => row['last_login'],
            sortable: true
        }
    ]

    componentDidMount() {
        fetch('http://localhost:8000/userlist/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(res => res.json())
            .then(data => {
                this.UserData = data;
                this.forceUpdate();
            })
    }

    render() {
        return (
            <DataTable
                title="Users"
                columns={this.Columns}
                data={this.UserData}
            />
        );
    }
}

export default Admin
// src/App.js
import React, { Component } from "react";
import axios from "axios";
import "./App.css";

class App extends Component {
  state = {
    products: [],
  };

  componentDidMount() {
    axios
      .get("http://localhost:8000/api/internet-products/")
      .then((res) => {
        this.setState({ products: res.data });
      })
      .catch((err) => {
        console.error(err);
      });
  }

  render() {
    return (
      <div className="App">
        <header>
          <h1>Catalogue Internet</h1>
        </header>
        <hr />
        <div className="product-list-container">
          <ul className="product-list">
            {this.state.products.map((product, id) => (
              <li key={id} className="product-item">
                <div className="product-name">{product.name}</div>
                <div className="product-brand">{product.brand}</div>
                <div className="product-price">{product.price} DH</div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    );
  }
}

export default App;

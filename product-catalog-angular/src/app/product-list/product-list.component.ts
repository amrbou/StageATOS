// src/app/product-list/product-list.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import axios from 'axios';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
  standalone: true,
  imports: [CommonModule]
})
export class ProductListComponent implements OnInit {
  products: any[] = [];

  constructor() {}

  ngOnInit(): void {
    this.fetchProducts();
  }

  fetchProducts() {
    axios.get('http://localhost:8000/api/internet-products/')
      .then(response => {
        this.products = response.data;
      })
      .catch(error => {
        console.error('There was an error fetching the products!', error);
      });
  }
}

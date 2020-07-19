import React from 'react';
import logo from './logo.svg';
import './App.css';
import {BookDisplay} from "./components/BookDisplay";

function App() {
  return (
    <BookDisplay bookId={1} />
  );
}

export default App;

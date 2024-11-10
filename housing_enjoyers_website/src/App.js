import './App.css';
import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Affordability from './pages/Affordability.js';
import Prediction from './pages/Prediction.js';
import Home from './pages/Home.js';


function App() {

	return (
		<div>
			<BrowserRouter>
				<Routes>
					<Route path='/' element={<Home/>} />
					<Route path='/Affordability' element={<Affordability/>} />
					<Route path='/Prediction' element={<Prediction/>} />
				</Routes>
			</BrowserRouter>
		</div>
  	);
}

export default App;

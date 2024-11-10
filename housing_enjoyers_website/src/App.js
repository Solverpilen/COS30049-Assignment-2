import './App.css';
import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Affordability from './pages/Affordability.js';
import Home from './pages/Home.js';


function App() {

	return (
		<div>
			<BrowserRouter>
				<Routes>
					<Route path='/' element={<Home/>} />
					<Route path='/Affordability' element={<Affordability/>} />
				</Routes>
			</BrowserRouter>
		</div>
  	);
}

export default App;

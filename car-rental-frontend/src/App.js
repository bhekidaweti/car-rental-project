import React from 'react';
import VehicleList from './VehicleList';
import BookingForm from './BookingForm';


import './App.css';

function App() {
  return (
    <div className="App">
   	<h1>Car Rental </h1>
	  <VehicleList />
	  <BookingForm />        
    </div>
  );
}

export default App;

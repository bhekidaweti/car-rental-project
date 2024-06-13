import React, { useState} from 'react';
import axios from 'axios';


function BookingForm(){
	const [vehicleId, setVehicleId] = useState('');
	const [startDate, setStartDate] = useState('');
	const [endDate, setEndDate] = useState('');


	const handleSubmit = (event) => {
		event.preventDefault();
		axios.post('http://localhost:8000/bookings/', {
			vehicle: vehicleId,
			start_date: startDate,
			end_date: endDate

		})
		.then(response => console.log(response))
		.catch(error => console.log(error));

	};

	return (
		
		<form onSubmit={handleSubmit}>
			<label>
				Vehicle ID:
				<input type="text" value={vehicleId} onChange={(e) => setVehicleId(e.target.value)} />
			</label>
			<label>
				Start Date:
				<input type="datetime-local" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
			</label>
			
		        <label>
				End Date:
				<input type="datetime-local" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
			</label>
			<button type="submit">Book a vehicle</button>
		</form>
	);

   }
export default BookingForm;

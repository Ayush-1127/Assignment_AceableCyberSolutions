import { useState } from "react";

const SearchForm = ({ onSearch }) => {
  const [query, setQuery] = useState("");
  const [startTime, setStartTime] = useState("");
  const [endTime, setEndTime] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
  
 
  const startTimeNum = Number(startTime);
  const endTimeNum = Number(endTime);

  if (!query || isNaN(startTimeNum) || isNaN(endTimeNum)) {
    alert("Please enter a valid query and numeric start/end times.");
    return;
  }

  onSearch({ query, startTime: startTimeNum, endTime: endTimeNum });
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-6 rounded-lg shadow-lg border border-gray-200 w-full max-w-xl mx-auto"
    >
      <h2 className="text-lg font-semibold text-gray-700 mb-4">Search Events</h2>
      
      <input
        type="text"
        placeholder="Enter search query (e.g., IP Address)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border border-gray-300 p-3 rounded-md w-full mb-4 focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />

      <div className="flex gap-4">
        <input
          type="number"
          placeholder="Start Time (Unix timestamp)"
          value={startTime}
          onChange={(e) => setStartTime(e.target.value)}
          className="border border-gray-300 p-3 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          placeholder="End Time (Unix timestamp)"
          value={endTime}
          onChange={(e) => setEndTime(e.target.value)}
          className="border border-gray-300 p-3 rounded-md w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <button
        type="submit"
        className="w-full mt-4 bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition duration-300"
      >
        Search
      </button>
    </form>
  );
};

export default SearchForm;

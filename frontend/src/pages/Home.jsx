import { useState } from "react";
import axios from "axios";
import SearchForm from "../components/SearchForm";
import ResultsTable from "../components/ResultsTable";

const Home = () => {
  const [results, setResults] = useState([]);
  const [searchTime, setSearchTime] = useState(0);

  const handleSearch = async (searchParams) => {
    const { query, startTime, endTime } = searchParams;

    console.log(" Raw Input Values:", { query, startTime, endTime });

    if (!startTime || !endTime) {
        console.error("Missing start time or end time!");
        return;
    }

    const startTimeSec = startTime;
    const endTimeSec = endTime;

    try {
        const start = performance.now();
        const response = await axios.post("http://127.0.0.1:8000/api/search/", 
            { query, start_time: startTimeSec, end_time: endTimeSec },
            { headers: { "Content-Type": "application/json" } }
        );
        const end = performance.now();

        console.log("API Response:", response.data);

        setResults(response.data.results);
        setSearchTime(parseFloat(((end - start) / 1000).toFixed(2)));

       
        console.log("Results before state update:", results);
        console.log("Search Time before state update:", searchTime);

    } catch (error) {
        console.error(" Error fetching search results:", error.response?.data || error);
    }
};



  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold text-blue-700 mb-6">Event Search System</h1>
      <SearchForm onSearch={handleSearch} />
      <ResultsTable results={results} searchTime={searchTime} />
    </div>
  );
};

export default Home;

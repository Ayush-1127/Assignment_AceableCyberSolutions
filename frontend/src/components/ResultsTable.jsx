import React from "react";

const ResultsTable = ({ results, searchTime }) => {
    return (
        <div className="p-4">
            <h2 className="text-lg font-semibold mb-4">Search Results</h2>
            <table className="w-full border-collapse border border-gray-300">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="border p-2">Event Found</th>
                        <th className="border p-2">Action</th>
                        <th className="border p-2">Log Status</th>
                        <th className="border p-2">File</th>
                        <th className="border p-2">Search Time</th>
                    </tr>
                </thead>
                <tbody>
                    {results.length > 0 ? (
                        results.map((log, index) => (
                            <tr key={index} className="border">
                                <td className="border p-2">{log.srcaddr} → {log.dstaddr}</td>
                                <td className="border p-2">{log.action}</td>
                                <td className="border p-2">{log.log_status}</td>
                                <td className="border p-2">{log.filename}</td>
                                <td className="border p-2">{searchTime.toFixed(2)} seconds</td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="5" className="border p-2 text-center">
                                No results found
                            </td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default ResultsTable;

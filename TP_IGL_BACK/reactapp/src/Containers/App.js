import React from "react";
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import AuthPage from './Authentification/index.js';
import AnnoncesPage from "./AnnoncesPage/index.js";
import ErrorPage from "./ErrorPage/index.js";
import PrivateRoute from "./PrivateRoute/index.js";

function App(){
    return(
        <Router>
            <Routes>
                <Route path="/" element={<AuthPage/>} />
                <Route path="/main" element={<PrivateRoute><AnnoncesPage/></PrivateRoute>} />
                <Route path="*" element={<ErrorPage/>} />
            </Routes>
        </Router>
    );
}
export default App;
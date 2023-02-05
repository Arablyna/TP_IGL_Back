import React from "react";
import { Navigate } from "react-router-dom";
import {useSelector} from 'react-redux';

const PrivateRoute = ({children}) => {
    const user = useSelector((state) => state.user.value);
    return (Object.keys(user).length != 0) ? children : <Navigate to="/" />;
}

export default PrivateRoute;
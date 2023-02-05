import React from "react";
import error from "./../../Assets/error.png";

const ErrorPage = () => {
    return(
        <div>
            <div className="Error">
                <img src={error} alt="Error 404"/>
            </div>
        </div>
    )
}

export default ErrorPage;
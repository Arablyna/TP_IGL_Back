import React from "react";
import { useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import {useDispatch, useSelector} from 'react-redux';
import { setCurrentUser } from "../../Redux/slices/currentUserSlice";
import AnnoncesPage from './../AnnoncesPage/index.js';
import logo from '../../Assets/logoSokna.png';
import { useNavigate } from "react-router-dom";

const AuthPage = () => {
    const currentUser = useSelector((state) => state.user.value);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleCallBackResponse = (response) => {
        var userObject = jwt_decode(response.credential);
        const userInfos = {
            "nom" : userObject["family_name"],
            "prenom" : userObject["given_name"],
            "email" : userObject["email"],
            "photo" : userObject["picture"]
        }
        // setUser(userInfos);
        dispatch(setCurrentUser(userInfos));
        // Upload user infos to BDD

        // document.getElementById("hero").hidden = true;
        // if (Object.keys(currentUser).length != 0){
        //     console.log(currentUser);
        navigate("./main");
    }

    const handleSignOut = (e) => {
        // setUser({});
        dispatch(setCurrentUser({}));
        // document.getElementById("hero").hidden = false;
    }

    useEffect(() => {
        /*global google*/
        google.accounts.id.initialize({
            client_id : "64942602411-9c3v2baidusqrppj68cmc43v66pp1a0k.apps.googleusercontent.com",
            callback : handleCallBackResponse
        });

        google.accounts.id.renderButton(
            document.getElementById("Signin"),
            {theme : "outline", size: "large"}
        );

        google.accounts.id.prompt();
    }, []);

    const [signIn, toggle] = React.useState(true);
     return(
        // <Route path='/' exact />
        <div className="App">
            <div className="HeroSection" id="hero">
                <div className="centre">
                    <div className="HeroInfos">
                        <div className="Title">
                            <img src={logo} alt="Logo"/>
                            <h1>Sokna</h1>
                        </div>
                        <p>Obtenez votre maison aujourd'hui</p>
                    </div>
                    <div id="Signin"></div>
                </div>
            </div>
            {/* {
                Object.keys(currentUser).length != 0 &&
                <AnnoncesPage/>
            } */}
        </div>
    //     <Router>
    //     <Layout>
    //       <Routes>
    //         <Route exact path="/" element={<Home/>}/>
    //         <Route exact path="/login" element={<Login/>}/>
    //         <Route exact path="/recovery-password" element={<RecoveryPassword/>}/>
    //         <Route path="*" element={<NotFound/>}/>
    //       </Routes>
    //     </Layout>
    //   </Router>
     )
}
export default AuthPage;

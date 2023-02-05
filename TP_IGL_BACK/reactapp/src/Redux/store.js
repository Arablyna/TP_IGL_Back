import { configureStore } from '@reduxjs/toolkit';
import currentUserSlice from './slices/currentUserSlice';

export default configureStore({
    reducer : {
        user : currentUserSlice,
    },
});
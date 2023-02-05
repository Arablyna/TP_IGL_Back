import { createSlice, configureStore } from '@reduxjs/toolkit'
// import { act } from 'react-dom/test-utils'

export const currentUserSlice = createSlice({
  name: 'currentUser',
  initialState: {
    value: {},
  },
  reducers: {
    setCurrentUser: (state, action) => {
      state.value = action.payload;
    },
  }
});

export const { setCurrentUser } = currentUserSlice.actions;

export default currentUserSlice.reducer;
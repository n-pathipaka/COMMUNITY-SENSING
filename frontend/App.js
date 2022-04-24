import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Survey from './components/Survey';
import Home  from './components/Home'
import Conntants from 'expo-constants';

//
// <Survey/>

export default function App() {
  return ( 
    <View style={style.con}>
      <Home />
      <StatusBar style="auto" />  
    </View>
  );
}


const style = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  con: {
    flex: 1,
    backgroundColor: '#eddfdf',
    marginTop:Conntants.statusBarHeight
  }
}); 

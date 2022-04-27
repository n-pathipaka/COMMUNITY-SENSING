import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Survey from './components/Survey';
import Home  from './components/Home';
import Submit from './components/Submit';
import Conntants from 'expo-constants';
import Main from './components/Main';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';


//
// <Survey/>

const Stack = createStackNavigator()

function App() {
  return ( 
    <View style={style.con}>
      <Stack.Navigator>
        <Stack.Screen name = "Main" component = {Main} />
        <Stack.Screen name = "Home" component = {Home} />
        <Stack.Screen name = "Submit" component = {Submit} />
      </Stack.Navigator>
      <StatusBar style="auto" />  
    </View>
  );
}

export default () => {

  return (
     <NavigationContainer>
       <App/>
     </NavigationContainer>

  )

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

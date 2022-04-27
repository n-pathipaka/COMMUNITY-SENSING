import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Conntants from 'expo-constants';
import {Button, Card} from 'react-native-paper';

import { useLinkProps } from '@react-navigation/native';

//
// <Survey/>


export default function Main(props) {
  return ( 
    <View style={style.container}>
        <Text style = {{fontSize:20}}> This survey is anonymus</Text>
      <Button 
           style = {{margin:20}}
           icon  = "pencil"
           mode  = "contained"
           onPress = {() => props.navigation.navigate('Home') }
       > Fill the survey </Button> 
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

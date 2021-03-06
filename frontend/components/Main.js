import { StyleSheet, Text, View } from 'react-native';
import {Button, Card} from 'react-native-paper';

//
// <Survey/>


export default function Main(props) {
  return ( 
    <View style={style.container}>
        <Card style = {style.cardStyle}>
        <Text style = {{fontSize:20}}> This is a POC deployed to 10 to 15 students to study the student belonginess. This survey is anonymous.</Text>
        </Card>
      <Button 
           style = {{margin:20}}
           icon  = "pencil"
           mode  = "contained"
           onPress = {() => props.navigation.navigate('Home') }
       > Fill the survey </Button> 
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
  },
  cardStyle : {
    margin: 10,
    padding: 10
}
}); 

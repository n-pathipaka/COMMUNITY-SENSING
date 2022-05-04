import { StyleSheet, Text, View, FlatList } from 'react-native';
import React, { useEffect, useState } from 'react';
import { Button } from 'react-native-paper';


export default function Submit(props){
    

    return (

        <View  style = {style.container}>  
            <Text style = {{fontSize:20}}> Thanks for submitting the survey    </Text>

            <Button 
           style = {{margin:20}}
           icon  = "pencil"
           mode  = "contained"
           onPress = {() => {
             props.navigation.navigate('Main')}}
             > Return Home </Button> 
 
        </View>
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
    }
  }); 
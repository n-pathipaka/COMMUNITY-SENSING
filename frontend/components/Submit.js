import { StyleSheet, Text, View, FlatList } from 'react-native';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Main from './Main';

export default function Submit(props){
    

    return (

        <View  style = {style.container}>  
            <Text style = {{fontSize:20}}> Thanks for submitting the survey    </Text>
            { props.navigation.navigate('Main')}
           
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
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, FlatList } from 'react-native';
import {useForm, Controller} from 'react-hook-form';
import RadioButton from './RadioButton';
import {Button, Card} from 'react-native-paper';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useLinkProps } from '@react-navigation/native';



 export default function Home(props) {

    //<RadioButton data={emotions} onSelect={(value) => setOption(value)} />

    const [backendData, setBackendData] = useState([])

    const[data, setQuestion] = useState([])

    const[options, setOption] = useState([])

    const url = 'http://10.0.0.146:5000/'

    const params = JSON.stringify({
        "user_id": "neerab"
    })

    const insertData = () => {
        console.log(data)
        console.log(options)
        props.navigation.navigate('Submit')
        
    } 

    /*
    headers:{
                'Content-Type':'apllication/json'
            },
            body: JSON.stringify({user_id:'neerab'}) */

    useEffect(() => {
        axios.post('http://10.0.0.146:5000/get_questions', {
            user_id : "neerab"
        })
        .then( function(response){
          //console.log(response['data'])
         
         setQuestion(response['data'])} )
        /*
        .then(q => {
            console.log(q)
            setQuestion(q)
        }) */
    } , [])
    /*
    const data = [
        {survey_id:1, question_id :1 , question: "How are you Feeling"},
        {survey_id:1, question_id :2 , question: "Are you using Library stuff"},
        {survey_id:1, question_id :3 ,question: "How faculty supporting"}
    ]  */

    /*
    renderOptions = {([option]) => {
                console.log(option)
            }} */

    const renderData = (item) => {
        var backendItemData = {}
        backendItemData['qid'] = item.question_id
        return (
            <View>
          <Card style = {style.cardStyle}>
            <Text style = {{fontSize: 18}}> {item.question} </Text>
            <RadioButton data={item.options} onSelect={(value) => {
                setOption(value)
                backendItemData['opt'] = value
                setBackendData(existingBackendData => [...existingBackendData, backendItemData])
            }
            } 
            /> 
          </Card>
          </View>
        )
      }
      /*
      const renerOptions = (items) => {
          return (
              <Text> {</Text>
          )
      } */

    return ( 
        
        <View style={{flex: 1,flexDirection: 'column', padding: 8}}>
            {console.log("Hello")}
            <Text> My name is neerab</Text>
        <FlatList
         data = {data}
         renderItem = {({item}) => {
             
             return renderData(item)
             
         }} 
         keyExtractor = {item => `${item.question_id}`}
     
       />

       <Button 
           style = {{margin:20}}
           icon  = "pencil"
           mode  = "contained"
           onPress = {() => insertData()}
       > Submit </Button> 
       </View>
    );
  }

  const style = StyleSheet.create({
        cardStyle : {
            margin: 10,
            padding: 10
        }


  })
  
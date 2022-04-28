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

    const[survey, setSurvey]  = useState([])

    const[user, setUserId] = useState([])

    const[noofquestions, setNumber] = useState([])
 
    const url = 'http://10.0.0.146:5000/'

    const [deviceId, setDeviceId] = useState([]);

    const getdeviceId = () => {
       console.log("Anuhya")
    };

    const sendData = () => {
        axios.post('http://35.239.141.186:5000/get_answers', {
            backendData,
            survey,
            user,
            noofquestions
        }
           
        )
        .then(function(response){
            console.log(survey)
            props.navigation.navigate('Submit')
         } )       
    }
    
    /*
    const insertData = () => {
        console.log(backendData)
        props.navigation.navigate('Submit')
        
    }  */

    /*
    headers:{
                'Content-Type':'apllication/json'
            },
            body: JSON.stringify({user_id:'neerab'}) */

    useEffect(() => {
        axios.post('http://35.239.141.186:5000/get_questions', {
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
        
        return (
            <View>
          <Card style = {style.cardStyle}>
            <Text style = {{fontSize: 18}}> {item.question} </Text>
            <Card style = {style.cardStyle}>
            <RadioButton data={item.options} onSelect={(value) => {
                setOption(value)
                backendItemData[item.question_id] = value
                setBackendData(existingBackendData => [...existingBackendData, backendItemData])
            }
            } 
            /> 
            </Card>
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
            { getdeviceId()}
            {console.log("Hello")}
        <FlatList
         data = {data}
         renderItem = {({item}) => {
             
             setSurvey(item.survey_id)
             setNumber(item.num)
             setUserId("neerab")
             return renderData(item)
             
         }}     
         keyExtractor = {item => `${item.question_id}`}
     
       />
       
       <Button 
           style = {{margin:20}}
           icon  = "pencil"
           mode  = "contained"
           onPress = {() => {
            sendData()}}
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
  
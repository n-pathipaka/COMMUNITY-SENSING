import { StatusBar } from 'expo-status-bar';
import React, { useEffect } from 'react';
import {useState} from 'react';
import { StyleSheet,  Button, Text, ScrollView , FlatList, View} from 'react-native';
import {useForm, Controller} from 'react-hook-form';
import RadioButton from './RadioButton';
import {Card} from 'react-native-paper';



export default function Survey(){

  const [data,setData] = useState([])
  /*
  useEffect(() => {
    fetch('', {
      method:'GET'
    })
    .then(resp => resp.json())
    .then(question => {
      setData(question)
    })
  }, []) */

  const question = [
      {survey_id:1, question_id: 1, question: "How are you Feeling"},
      {survey_id:1, question_id: 2, question: "Are you using Library stuff"},
      {survey_id:1, question_id: 3, question: "How faculty supporting"},
  ]

    const emotions = [
        { value: 'Happy'},
        { value: 'Sad' },
        { value: 'Anxious'}
    ]

    const location = [
      {value: 'Rec Center'},
      {value: 'UMC'},
      {value: 'CommunityCenter'}
    ]
    const [option, setOption] = useState(null);

    const renderData = (item) => {
      return (
        <Card>
          <Text> item.question_id</Text>
          <Text> item.question </Text>
        </Card>
      )
    }

    // TODO(Neerab):
    // 1. Add a submit handler for your submit button and implement the backend logic in that function
    // 2. use Mutiple options(i.e., an array of options) for your radio buttons and questions.
    // 3. Improve the user interface by changing the style before creating the app.
    return (
       
      /*
      <ScrollView style={styles.container}>
        <Text style={styles.question}>Choose your current mood: </Text>
        <RadioButton data={emotions} onSelect={(value) => setOption(value)} />

        <Text style={styles.question}>Where are you right now? </Text>
        <RadioButton data={location} onSelect={(value) => setOption(value)} />

        <Button 
          title="Submit"
          color="#841584"
        /> 
        
         </ScrollView>*/
        <View style = {styles.textStyle}>
        <FlatList
         question = {question}
         renderItem = {({item}) => {
        return renderData(item)
         }} 
         keyExtractor = {item => `${item.survey_id}`}
     
       />
       </View>

    );

};


const styles = StyleSheet.create({
    container: {
      marginTop: 100,
      height: '100%',
      width: 'auto',
    },
    question: {
      padding: 10
    },
    textStyle:{
      color:'brown',
      padding:10,
      margin:20,
      fontSize:25
    }
  });
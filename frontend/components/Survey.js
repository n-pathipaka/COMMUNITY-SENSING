import { StatusBar } from 'expo-status-bar';
import React from 'react';
import {useState} from 'react';
import { StyleSheet,  Button, Text, ScrollView } from 'react-native';
import {useForm, Controller} from 'react-hook-form';
import RadioButton from './RadioButton';


export default function Survey(){
    const emotions = [
        { value: 'Happy'},
        { value: 'Sad' },
        { value: 'Anxious'}
    ]

    const locations = [
      {value: 'Rec Center'},
      {value: 'UMC'},
      {value: 'CommunityCenter'}
    ]
    const [option, setOption] = useState(null);

    // TODO(Neerab):
    // 1. Add a submit handler for your submit button and implement the backend logic in that function
    // 2. use Mutiple options(i.e., an array of options) for your radio buttons and questions.
    // 3. Improve the user interface by changing the style before creating the app.
    return (
      <ScrollView style={styles.container}>
        <Text style={styles.question}>Choose your current mood: </Text>
        <RadioButton data={emotions} onSelect={(value) => setOption(value)} />

        <Text style={styles.question}>Where are you right now? </Text>
        <RadioButton data={location} onSelect={(value) => setOption(value)} />

        <Button 
          title="Submit"
          color="#841584"
        />

      </ScrollView>
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
    }
  });
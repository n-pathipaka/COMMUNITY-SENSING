import { StatusBar } from 'expo-status-bar';
import { StyleSheet,  Button,TextInput, Text, View } from 'react-native';
import {SimpleSurvey} from 'react-native-simple-survey';


const questions = [
    {
        questionType: 'Info',
        questionText: 'Welcome to the React Native Simple Survey Example app! Tap next to continue'
    },
    {
      questionType: 'SelectionGroup',
      questionText: 'Simple Survey also has multiple choice questions. What is your favorite pet?',
      questionId: 'favoritePet',
      options: [
          {
              optionText: 'Dogs',
              value: 'dog'
          },
          {
              optionText: 'Cats',
              value: 'cat'
          },
          {
              optionText: 'Ferrets',
              value: 'ferret'
          },
      ]
  },
  {
    questionType: 'NumericInput',
    questionText: 'It also supports numeric input. Enter your favorite number here!',
    questionId: 'favoriteNumber',
    placeholderText: '',
},
    {
        questionType: 'TextInput',
        questionText: 'Simple Survey supports free form text input',
        questionId: 'favoriteColor',
        placeholderText: 'Tell me your favorite color!',
    }
];

const renderInfoText = (infoText) => {
    return (<Text style={styles.infoText}>{infoText}</Text>);
  };

  const renderTextInput = (onChange, value, placeholder, onBlur) => {
    return (<TextInput
      onChangeText={text => onChange(text)}
      value={value}
      placeholder={placeholder}
      onBlur={onBlur}
    />);
  };

export default function Survey(){
    return (
        <SimpleSurvey
    survey={questions}
    selectionGroupContainerStyle={styles.selectionGroupContainer}
    renderTextInput={renderTextInput}
    renderInfo={renderInfoText}
    renderNumericInput={this.renderNumericInput}
/>
      );

};

const renderNumericInput = (onChange, value, placeholder, onBlur) => {
  return (<TextInput 
    style={styles.numericInput}
    onChangeText={text => { onChange(text); }}
    underlineColorAndroid={'white'}
    placeholderTextColor={'rgba(184,184,184,1)'}
    placeholder={placeHolder}
    value={String(value)}
    keyboardType={'numeric'}
    maxLength={3}
    onBlur={onBlur}
  />);
}


const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    infoText: {
        fontSize: 10
    }
  });
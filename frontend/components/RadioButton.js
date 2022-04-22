import React from 'react';
import {useState} from 'react';
import {View, Text, Pressable } from 'react-native';
import styles from './Styles';

export default function RadioButton({data, onSelect}) {
  const [userOption, setUserOption] = useState(null)

  const selectHandler = (value) => {
    onSelect(value);
    setUserOption(value)
  }
  return (
    <View>
      {data.map((item) => {
        return (
          <Pressable 
            style = {
              item.value === userOption ? styles.selected : styles.unselected
            }
            onPress = { () => selectHandler(item.value)}>
            <Text>{item.value}</Text>
          </Pressable>
        )
      })}
    </View>
  )
}
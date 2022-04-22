import { StyleSheet } from "react-native";
const styles = StyleSheet.create({
  option: {
    fontSize: 20,
    color: "white",
    textAlign: "center",
  },
  unselected: {
    borderColor: "grey",
    margin: 5,
  },
  selected: {
    backgroundColor: "#EDEDED",
    marginTop: 6,
    paddingTop: 10,
    paddingBottom: 10,
    paddingRight: 10,
    paddingLeft: 10,
    borderRadius: 10,
  },
});
export default styles;

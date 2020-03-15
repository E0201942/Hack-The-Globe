import React, { Component } from "react";
import {
  Dimensions,
  Image,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  View
} from "react-native";

import Slider from "react-native-slider";

import { Divider, Card, Badge, Button, Block, Text } from "../components";
import { theme, mocks } from "../constants";

const { width } = Dimensions.get("window");

class HomePage extends Component {
  state = {
    active: "Products",
    categories: [],
    budget: 850,
    monthly: 1700,
  };

  componentDidMount() {
    const { categories } = this.props;
    const filtered = categories.filter(category =>
      category.tags.includes("supermarkets")
    );

    this.setState({ categories: filtered });
  }


  render() {
    const { profile, navigation } = this.props;
    const { categories } = this.state;

    return (
      <View>
        <Image source={require("../assets/HomePage.png")} resizeMode={'cover'} style={styles.imageContainer}></Image>
      </View>
    );
  }
}

HomePage.defaultProps = {
  profile: mocks.profile,
  categories: mocks.categories
};

export default HomePage;

const styles = StyleSheet.create({
  header: {
    paddingHorizontal: theme.sizes.base * 2
  },
  avatar: {
    height: theme.sizes.base * 2.2,
    width: theme.sizes.base * 2.2
  },
  tabs: {
    borderBottomColor: theme.colors.gray2,
    borderBottomWidth: StyleSheet.hairlineWidth,
    marginVertical: theme.sizes.base,
    marginHorizontal: theme.sizes.base * 2
  },
  tab: {
    marginRight: theme.sizes.base * 2,
    paddingBottom: theme.sizes.base
  },
  active: {
    borderBottomColor: theme.colors.secondary,
    borderBottomWidth: 3
  },
  categories: {
    flexWrap: "wrap",
    paddingHorizontal: theme.sizes.base * 2,
    marginBottom: theme.sizes.base * 3.5
  },
  category: {
    // this should be dynamic based on screen width
    minWidth: (width - theme.sizes.padding * 2.4 - theme.sizes.base) / 2,
    maxWidth: (width - theme.sizes.padding * 2.4 - theme.sizes.base) / 2,
    maxHeight: (width - theme.sizes.padding * 2.4 - theme.sizes.base) / 2
  },
  imageContainer: {
    alignSelf: 'center',
    height: '100%',
    width: '100%'
  },
  sliders: {
    marginTop: theme.sizes.base * 0.7,
    paddingHorizontal: theme.sizes.base * 2
  },
});

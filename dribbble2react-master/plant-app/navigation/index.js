import React from "react";
import { Image, View } from "react-native";
import { createAppContainer, createSwitchNavigator } from 'react-navigation';
import { createStackNavigator } from "react-navigation-stack";
import { createBottomTabNavigator } from 'react-navigation-tabs';
import {Colors} from 'react-native/Libraries/NewAppScreen'
import { createMaterialBottomTabNavigator } from 'react-navigation-material-bottom-tabs'
import { Ionicons } from '@expo/vector-icons';

import Login from '../screens/Login';
import Welcome from "../screens/Welcome";
import SignUp from "../screens/SignUp";
import Forgot from "../screens/Forgot";
import Explore from "../screens/Explore";
import Browse from "../screens/Browse";
import Product from "../screens/Product";
import Settings from "../screens/Settings";
import HomePage from "../screens/HomePage"
import Team from "../screens/Team"

import { theme } from "../constants";

const AuthStack = createStackNavigator(
  {
    Welcome,
    Login,
    SignUp,
    Forgot,
  }

);

const AppStack = createStackNavigator(
  {
    Explore,
    Browse,
    Product,
    Settings
  },
  {
    headerMode: 'none'

  }
);

const HomeStack = createStackNavigator(
  {
    HomePage
  },
  {
    headerMode: 'none'

  }
);

const TeamStack = createStackNavigator(
  {
    Team
  },
  {
    headerMode: 'none'

  }
);

const TabNavigator = createMaterialBottomTabNavigator(
  {
    Home: {
      screen: HomeStack,
    },
    Team: {
      screen: Team
    },
    Shop: {
      screen: AppStack
    },
    Rewards: {
      screen: AppStack
    },
    Profile: {
      screen: Settings
    },
    StoreLocator: {
      screen: AuthStack
    },
  },
  {
    labeled: true,
    shifting: false,
    initialRouteName: "Home",
    barStyle: { backgroundColor: '#3BAD87' },
  },
);

const TabStack = createStackNavigator({
  Tabs: TabNavigator
});

const AppNavigator = createSwitchNavigator(
  {
    Auth: AuthStack,
    Home: TabStack,
  },

);
// const screens = createStackNavigator(
//   {
//     Welcome,
//     Login,
//     SignUp,
//     Forgot,
//     Explore,
//     Browse,
//     Product,
//     Settings
//   },
//   {
//     defaultNavigationOptions: {
//       headerStyle: {
//         height: theme.sizes.base * 4,
//         backgroundColor: theme.colors.white, // or 'white
//         borderBottomColor: "transparent",
//         elevation: 0 // for android
//       },
//       headerBackImage: <Image source={require("../assets/icons/back.png")} />,
//       headerBackTitle: null,
//       headerLeftContainerStyle: {
//         alignItems: "center",
//         marginLeft: theme.sizes.base * 2,
//         paddingRight: theme.sizes.base
//       },
//       headerRightContainerStyle: {
//         alignItems: "center",
//         paddingRight: theme.sizes.base
//       }
//     }
//   }
// );

export default createAppContainer(AppNavigator);

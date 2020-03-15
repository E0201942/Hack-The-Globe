const categories = [
  {
    id: "1",
    name: "Giant",
    tags: ["supermarkets"],
    info: '',
    image: require("../assets/icons/giant_logo.png")
  },
  {
    id: "2",
    name: "FairPrice",
    tags: ["supermarkets"],
    info: '',
    image: require("../assets/icons/fairprice_logo.png")
  },
  {
    id: "3",
    name: "Cold Storage",
    tags: ["supermarkets"],
    info: '',
    image: require("../assets/icons/coldstorage_logo.jpg")
  },
  {
    id: "4",
    name: "Prime",
    tags: ["supermarkets"],
    info: '',
    image: require("../assets/icons/prime_logo.jpg")
  },
  {
    id: "5",
    name: "Sheng Siong",
    tags: ["supermarkets"],
    info: '',
    image: require("../assets/icons/shengsiong_logo.png")
  },
  {
    id: "6",
    name: "Paragon Market",
    tags: ["supermarkets"],
    info: '',
    image: require("../assets/icons/paragon_logo.png")
  },
  {
    id: "giant1",
    name: "Giant",
    tags: ["promotions"],
    info: "Mar 13 - Mar 26",
    image: require("../assets/icons/giant1.png")
  },
  {
    id: "giant2",
    name: "Giant",
    tags: ["promotions"],
    info: "Mar 06 - Mar 19",
    image: require("../assets/icons/giant2.png")
  },
  {
    id: "ntuc",
    name: "Fairprice",
    tags: ["promotions"],
    info: "Mar 06 - Mar 19",
    image: require("../assets/icons/ntuc.png")
  },
  {
    id: "coldstorage",
    name: "Cold Storage",
    tags: ["promotions"],
    info: "Feb 28 - Mar 02",
    image: require("../assets/icons/coldstorage.png")
  },
  {
    id: "shengsiong",
    name: "Sheng Siong",
    tags: ["promotions"],
    info: "Mar 06 - Mar 19",
    image: require("../assets/icons/shengshiong.png")
  },
  {
    id: "prime",
    name: "Prime",
    tags: ["promotions"],
    info: "Mar 06 - Mar 19",
    image: require("../assets/icons/prime.png")
  }
];

const products = [
  {
    id: 1,
    name: "16 Best Plants That Thrive In Your Bedroom",
    description:
      "Bedrooms deserve to be decorated with lush greenery just like every other room in the house – but it can be tricky to find a plant that thrives here. Low light, high humidity and warm temperatures mean only certain houseplants will flourish.",
    tags: ["Interior", "27 m²", "Ideas"],
    images: [
      require("../assets/images/plants_1.png"),
      require("../assets/images/plants_2.png"),
      require("../assets/images/plants_3.png"),
      // showing only 3 images, show +6 for the rest
      require("../assets/images/plants_1.png"),
      require("../assets/images/plants_2.png"),
      require("../assets/images/plants_3.png"),
      require("../assets/images/plants_1.png"),
      require("../assets/images/plants_2.png"),
      require("../assets/images/plants_3.png")
    ]
  }
];

const explore = [
  // images
  require("../assets/images/explore_1.png"),
  require("../assets/images/explore_2.png"),
  require("../assets/images/explore_3.png"),
  require("../assets/images/explore_4.png"),
  require("../assets/images/explore_5.png"),
  require("../assets/images/explore_6.png")
];

const profile = {
  username: "react-ui-kit",
  location: "Europe",
  email: "contact@react-ui-kit.com",
  avatar: require("../assets/images/avatar.png"),
  budget: 1000,
  monthly_cap: 5000,
  notifications: true,
  newsletter: false
};

export { categories, explore, products, profile };

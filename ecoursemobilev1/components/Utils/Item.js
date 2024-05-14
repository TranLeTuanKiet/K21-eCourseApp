import { List } from "react-native-paper";
import MyStyles from "../../styles/MyStyles";

const Item = () => {
    return (
        <List.Item style={MyStyles.margin} title={instance.subject}
                    description={instance}/>
    )
}

export default Item;
import { useFonts } from 'expo-font';
import * as SplashScreen from 'expo-splash-screen';
import 'react-native-reanimated';
import { Slot, Tabs } from 'expo-router';
import { DarkTheme, DefaultTheme, ThemeProvider } from '@react-navigation/native';
import { useColorScheme } from '@/hooks/useColorScheme';
import { StyleSheet, Text } from 'react-native';
import { Ionicons } from '@expo/vector-icons'; // Import Ionicons from @expo/vector-icons
import { useEffect } from "react";
import SignIn from '../sign-in';
import { useAuth } from '@/providers/AuthProvider';

export default function TabsLayout() {
    const { loggedIn } = useAuth();
    const colorScheme = useColorScheme();
    const [loaded] = useFonts({
        SpaceMono: require('../../assets/fonts/SpaceMono-Regular.ttf'),
    });

    useEffect(() => {
        if (loaded) {
            SplashScreen.hideAsync();
        }

    }, [loaded]);

    if (!loaded) {
        return null;
    }

    if (!loggedIn) {
        return <SignIn />;
    }

    return (
        <ThemeProvider value={colorScheme === 'dark' ? DarkTheme : DefaultTheme}>
            <Tabs initialRouteName='index'
                screenOptions={({ route }) => ({

                    tabBarIcon: ({ focused, color, size }) => {

                        let iconName: keyof typeof Ionicons.glyphMap | undefined;

                        if (route.name === 'index') {
                            iconName = focused ? 'apps' : 'apps-outline';
                        } else if (route.name === 'feed') {
                            iconName = focused ? 'send' : 'send-outline';
                        } else if (route.name === 'classes') {
                            iconName = focused ? 'albums' : 'albums-outline';
                        } else if (route.name === 'setting') {
                            iconName = focused ? 'cog' : 'cog-outline';
                        }

                        return <Ionicons name={iconName} size={size} color={color} />;
                    },
                    tabBarActiveTintColor: 'blue',
                    tabBarInactiveTintColor: 'gray',
                })}
            >
                <Tabs.Screen name="index" options={{
                    headerShown: false,
                    tabBarLabel: "Dashboard",
                }} />
                <Tabs.Screen name="feed" options={{
                    headerShown: false,
                    tabBarLabel: "Feed",
                }} />
                <Tabs.Screen name="classes" options={{
                    headerShown: false,
                    tabBarLabel: "Classes",
                }} />
                <Tabs.Screen name='setting' options={{
                    headerShown: false,
                    tabBarLabel: "Settings",
                }} />
            </Tabs>

        </ThemeProvider>
    );
}

const styles = StyleSheet.create({
    text: {
        color: "white"
    }
});
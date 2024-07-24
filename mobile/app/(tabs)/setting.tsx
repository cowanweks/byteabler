import React from 'react';
import { StyleSheet, View, TouchableOpacity, Alert, Switch } from 'react-native';
import { ThemedText } from "@/components/ThemedText";
import { ThemedView } from "@/components/ThemedView";
import { SafeAreaView } from "react-native-safe-area-context";
import { useAuth } from "@/providers/AuthProvider";
import SignIn from '@/app/sign-in';
import { Ionicons } from "@expo/vector-icons";
import { useState } from 'react';

const Setting: React.FC = () => {
    const { loggedIn, setLoggedIn } = useAuth();
    const [notificationsEnabled, setNotificationsEnabled] = useState(true);
    const [darkTheme, setDarkTheme] = useState(false);

    if (!loggedIn) {
        return <SignIn />; // Render sign-in screen if not logged in
    }

    const handleSignOut = () => {
        Alert.alert(
            "Sign Out",
            "Are you sure you want to sign out?",
            [
                {
                    text: "Cancel",
                    style: "cancel",
                },
                {
                    text: "Sign Out",
                    onPress: () => {
                        setLoggedIn(false); // Assuming setLoggedIn is used to manage authentication state
                    },
                },
            ],
            { cancelable: false }
        );
    };

    return (
        <SafeAreaView style={styles.container}>
            <ThemedView style={styles.header}>
                <Ionicons name="cog-outline" size={24} color="tomato" />
                <ThemedText style={styles.headerText}>Settings</ThemedText>
            </ThemedView>

            <ThemedView style={styles.settingsContainer}>
                <View style={styles.settingItem}>
                    <ThemedText style={styles.settingText}>Enable Notifications</ThemedText>
                    <Switch
                        value={notificationsEnabled}
                        onValueChange={setNotificationsEnabled}
                    />
                </View>

                <View style={styles.settingItem}>
                    <ThemedText style={styles.settingText}>Dark Theme</ThemedText>
                    <Switch
                        value={darkTheme}
                        onValueChange={setDarkTheme}
                    />
                </View>

                <TouchableOpacity style={styles.signOutButton} onPress={handleSignOut}>
                    <ThemedText style={styles.signOutText}>Sign Out</ThemedText>
                </TouchableOpacity>
            </ThemedView>
        </SafeAreaView>
    );
};

export default Setting;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
    header: {
        flexDirection: 'row',
        alignItems: 'center',
        padding: 16,
        backgroundColor: '#f8f8f8',
    },
    headerText: {
        marginLeft: 8,
        fontSize: 18,
        fontWeight: 'bold',
        color: 'black'
    },
    settingsContainer: {
        padding: 16,
    },
    settingItem: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        paddingVertical: 12,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
    },
    settingText: {
        fontSize: 16,
        color: '#333',
    },
    signOutButton: {
        marginTop: 20,
        paddingVertical: 12,
        backgroundColor: 'tomato',
        borderRadius: 8,
        alignItems: 'center',
    },
    signOutText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
    }
});

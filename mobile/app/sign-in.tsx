import { router, Stack } from 'expo-router';
import { StyleSheet, TextInput, Button, Alert, View, TouchableOpacity } from 'react-native';
import { useState } from 'react';

import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';

import { signIn } from "@/services/users"
import { FontAwesome } from "@expo/vector-icons";
import { useAuth } from "@/providers/AuthProvider";

export default function SignIn() {
    const [username, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);

    const { setLoggedIn } = useAuth()


    const handleSignIn = async () => {

        if (username == '') { Alert.alert('Required Field', "UserName is  Required!"); return }
        if (password == '') { Alert.alert('Required Field', "Password is  Required!"); return }

        const response = await signIn({ username: username, password: password });

        if (response) {
            Alert.alert('Sign In Successful', 'You have successfully signed in!');
            setLoggedIn(true);
            router.push("(tabs)");

        } else {
            Alert.alert('Sign In Failed', 'Please check your credentials and try again.');
        }
    };

    return (
        <>
            <Stack.Screen options={{ title: 'Sign In' }} />
            <ThemedView style={styles.container}>

                <ThemedText style={styles.title}>Sign In</ThemedText>

                <TextInput
                    style={styles.input}
                    placeholder="UserName"
                    value={username}
                    onChangeText={setUserName}
                    autoCapitalize="none"
                    placeholderTextColor="#888"
                />
                <View style={styles.passwordContainer}>
                    <TextInput
                        style={styles.inputPassword}
                        placeholder="Password"
                        value={password}
                        onChangeText={setPassword}
                        secureTextEntry={!showPassword}
                        autoCapitalize="none"
                        placeholderTextColor="#888"
                    />
                    <TouchableOpacity
                        style={styles.showPasswordButton}
                        onPress={() => setShowPassword(!showPassword)}
                    >
                        <ThemedText style={styles.showPasswordText}>
                            {showPassword ? <FontAwesome name='eye-slash' /> : <FontAwesome name='eye' />}
                        </ThemedText>
                    </TouchableOpacity>
                </View>
                <TouchableOpacity style={styles.button} onPress={handleSignIn}>
                    <ThemedText style={styles.buttonText}>Sign In</ThemedText>
                    {/* <HideIcon /> */}
                </TouchableOpacity>
            </ThemedView>
        </>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        padding: 20,
        backgroundColor: '#f5f5f5',
    },
    title: {
        fontSize: 32,
        height: 20,
        fontWeight: 'bold',
        marginBottom: 20,
        color: '#6200EE',
    },
    input: {
        width: '100%',
        padding: 15,
        marginVertical: 10,
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 4,
        backgroundColor: '#fff',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 5,
        elevation: 3,
    },
    passwordContainer: {
        width: '100%',
        position: 'relative',
    },
    inputPassword: {
        width: '100%',
        padding: 15,
        marginVertical: 10,
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 10,
        backgroundColor: '#fff',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 5,
        elevation: 3,
    },
    showPasswordButton: {
        position: 'absolute',
        right: 15,
        top: 25,
    },
    showPasswordText: {
        color: '#6200EE',
    },
    button: {
        width: '100%',
        padding: 15,
        marginVertical: 10,
        backgroundColor: '#6200EE',
        borderRadius: 4,
        alignItems: 'center',
        justifyContent: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 5,
        elevation: 3,
    },
    buttonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
    },
    linkContainer: {
        marginTop: 20,
    },
    link: {
        color: '#6200EE',
        fontSize: 16,
    },
});

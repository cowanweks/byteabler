import React, { useEffect, useState } from "react";
import { Text, StyleSheet, FlatList, View, ListRenderItem } from "react-native";
import { ThemedView } from "@/components/ThemedView";
import { ThemedText } from "@/components/ThemedText";
import { SafeAreaView } from 'react-native-safe-area-context';
import { FontAwesome, Ionicons } from "@expo/vector-icons";
import { useAuth } from "@/providers/AuthProvider";
import SignIn from '@/app/sign-in';

interface Class {
    id: string;
    name: string;
    time: string;
}

const classesMockData: Class[] = [
    { id: '1', name: 'Math 101', time: '09:00 AM - 10:00 AM' },
    { id: '2', name: 'Physics 201', time: '11:00 AM - 12:00 PM' },
    { id: '3', name: 'Chemistry 301', time: '01:00 PM - 02:00 PM' },
    { id: '4', name: 'Biology 401', time: '03:00 PM - 04:00 PM' }
];

export default function ClassPage() {

    const { loggedIn } = useAuth();
    const [classes, setClasses] = useState<Class[]>([]);

    useEffect(() => {
        // Fetch data here and update the state
        // Example: fetchClasses();
        // For now, we will use mock data
        setClasses(classesMockData);
    }, []);

    if (!loggedIn) {
        return <SignIn />; // Render sign-in screen if not logged in
    }

    const renderClassItem: ListRenderItem<Class> = ({ item }) => (
        <View style={styles.classItem}>
            <View style={{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                columnGap: 8
            }}>
                <Ionicons name="book-outline" size={18} />
                <ThemedText style={styles.className}>{item.name}</ThemedText>
            </View>
            <View style={{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                columnGap: 8
            }}>
                <Ionicons name="time-outline" size={18} />
                <ThemedText style={styles.classTime}>{item.time}</ThemedText>
            </View>
        </View>
    );

    return (
        <SafeAreaView style={styles.container}>
            <ThemedView style={styles.header}>
                <FontAwesome name="calendar" size={24} color="tomato" />
                <ThemedText style={styles.headerText}>Upcoming Classes</ThemedText>
            </ThemedView>
            <FlatList
                data={classes}
                renderItem={renderClassItem}
                keyExtractor={(item) => item.id}
                contentContainerStyle={styles.classesList}
            />
        </SafeAreaView>
    );
};


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
    classesList: {
        padding: 16,
    },
    classItem: {
        padding: 16,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
    },
    className: {
        fontSize: 16,
        color: '#000',
        fontWeight: 'bold',
    },
    classTime: {
        fontSize: 14,
        color: '#666',
    },
});

import React, { useEffect, useState } from "react";
import { Text, StyleSheet, FlatList, View, ListRenderItem } from "react-native";
import { ThemedView } from "@/components/ThemedView";
import { ThemedText } from "@/components/ThemedText";
import { SafeAreaView } from 'react-native-safe-area-context';
import { FontAwesome, Ionicons } from "@expo/vector-icons";
import { useAuth } from "@/providers/AuthProvider";
import SignIn from '@/app/sign-in';
import { Lecture } from "@/types"
import { getLectures } from "@/services/lectures"


export default function ClassPage() {

    const { loggedIn, user, role } = useAuth();
    const [lectures, setLectures] = useState<Lecture[]>([]);

    useEffect(() => {

        const fetchLectures = async () => {

            const lectures = await getLectures({ role: role, user: user, day: undefined });
            setLectures(lectures)
        }

        fetchLectures();

    }, [lectures, role, user]);

    if (!loggedIn) {
        return <SignIn />; // Render sign-in screen if not logged in
    }

    const renderClassItem: ListRenderItem<Lecture> = ({ item }) => (
        <View style={styles.classItem}>
            <View style={{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                columnGap: 8
            }}>
                <Ionicons color="green" name="book-outline" size={18} />
                <ThemedText style={styles.className}>{item.unitCode}</ThemedText>
                <ThemedText style={styles.className}>{item.unitName}</ThemedText>
            </View>
            <View style={{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
                columnGap: 8
            }}>
                <Ionicons color="blue" name="time-outline" size={18} />
                <ThemedText style={styles.classTime}>{item.startTime}</ThemedText> - 
                <ThemedText style={styles.classTime}>{item.endTime}</ThemedText>
                <ThemedText style={styles.weekDay}>{item.weekDay}</ThemedText>
                <ThemedText style={styles.lecName}>{item.lecName}</ThemedText>
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
                data={lectures}
                renderItem={renderClassItem}
                keyExtractor={(item) => item.lectureId}
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
        fontWeight: 'semibold',
    },
    classTime: {
        fontSize: 14,
        color: '#666',
    },
    lecName: {
        fontSize: 14,
        color: '#666',
    },
    weekDay: {
        color: 'tomato'
    }
});

import React, { useEffect, useState } from "react";
import { StyleSheet, FlatList, View, ListRenderItem } from "react-native";
import { ThemedText } from "@/components/ThemedText";
import { ThemedView } from "@/components/ThemedView";
import { SafeAreaView } from "react-native-safe-area-context";
import { Ionicons } from "@expo/vector-icons";

interface FeedItem {
    id: string;
    title: string;
    description: string;
    type: 'class' | 'reschedule' | 'update'; // Example types of feed items
    timestamp: string;
}

const feedMockData: FeedItem[] = [
    { id: '1', title: 'New Class Added', description: 'Math 101 has been added to your schedule.', type: 'class', timestamp: '2024-07-23T09:00:00Z' },
    { id: '2', title: 'Class Rescheduled', description: 'Physics 201 has been rescheduled to 2:00 PM.', type: 'reschedule', timestamp: '2024-07-23T11:00:00Z' },
    { id: '3', title: 'New Update', description: 'Chemistry 301 will have a guest lecture next week.', type: 'update', timestamp: '2024-07-23T13:00:00Z' },
    { id: '4', title: 'New Class Added', description: 'Biology 401 has been added to your schedule.', type: 'class', timestamp: '2024-07-23T15:00:00Z' }
];

const Feed: React.FC = () => {
    const [feedItems, setFeedItems] = useState<FeedItem[]>([]);

    useEffect(() => {
        // Fetch data here and update the state
        // Example: fetchFeedItems();
        // For now, we will use mock data
        setFeedItems(feedMockData);
    }, []);

    const renderFeedItem: ListRenderItem<FeedItem> = ({ item }) => (
        <View style={styles.feedItem}>
            <ThemedText style={styles.feedTitle}>{item.title}</ThemedText>
            <ThemedText style={styles.feedDescription}>{item.description}</ThemedText>
            <ThemedText style={styles.feedTimestamp}>{new Date(item.timestamp).toLocaleString()}</ThemedText>
        </View>
    );

    return (
        <SafeAreaView style={styles.container}>
            <ThemedView style={styles.header}>
                <Ionicons name="layers-outline" size={24} color="tomato" />
                <ThemedText style={styles.headerText}>Feed</ThemedText>
            </ThemedView>
            <FlatList
                data={feedItems}
                renderItem={renderFeedItem}
                keyExtractor={(item) => item.id}
                contentContainerStyle={styles.feedList}
            />
        </SafeAreaView>
    );
};

export default Feed;

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
    feedList: {
        padding: 16,
    },
    feedItem: {
        padding: 16,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
    },
    feedTitle: {
        fontSize: 16,
        color: '#000',
        fontWeight: 'bold',
    },
    feedDescription: {
        fontSize: 14,
        color: '#666',
    },
    feedTimestamp: {
        fontSize: 12,
        color: '#aaa',
    },
});

import React, { useEffect, useState } from "react";
import { StyleSheet, View, FlatList, ListRenderItem } from "react-native";
import { ThemedText } from "@/components/ThemedText";
import { ThemedView } from "@/components/ThemedView";
import { SafeAreaView } from "react-native-safe-area-context";
import { useAuth } from "@/providers/AuthProvider";
import SignIn from '@/app/sign-in';
import { Ionicons, Feather as Feathericons } from "@expo/vector-icons";
import { GestureHandlerRootView } from "react-native-gesture-handler";

interface Class {
    id: string;
    name: string;
    time: string;
}

interface Feed {
    id: string;
    title: string;
    time: string;
}

const classesMockData: Class[] = [
    { id: '1', name: 'Math 101', time: '09:00 AM - 10:00 AM' },
    { id: '2', name: 'Physics 201', time: '11:00 AM - 12:00 PM' },
    { id: '3', name: 'Chemistry 301', time: '01:00 PM - 02:00 PM' },
    { id: '4', name: 'Biology 401', time: '03:00 PM - 04:00 PM' }
];

const feedMockData: Feed[] = [
    { id: '1', title: 'Math 101 Re-Scheduled', time: '09:00 AM - 10:00 AM' },
];

const DashboardPage: React.FC = () => {
    const { loggedIn } = useAuth();
    const [classes, setClasses] = useState<Class[]>([]);
    const [feed, setFeed] = useState<Feed[]>([]);

    useEffect(() => {
        // Fetch data here and update the state
        setClasses(classesMockData);
        setFeed(feedMockData);
    }, []);

    if (!loggedIn) {
        return <SignIn />; // Render sign-in screen if not logged in
    }

    const renderClassItem: ListRenderItem<Class> = ({ item }) => (
        <View style={styles.classItem}>
            <View style={styles.classInfo}>
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
        </View>
    );
    const renderFeedItem: ListRenderItem<Feed> = ({ item }) => (
        <View style={styles.classItem}>
            {/* <Ionicons name="book-outline" size={24} color="black" style={styles.icon} /> */}
            <View style={styles.classInfo}>
                <ThemedText style={styles.className}>{item.title}</ThemedText>
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
        </View>
    );

    const renderClassSectionHeader = (title: string, icon: React.ReactNode) => (
        <ThemedView style={styles.section}>
            <View style={styles.sectionHeader}>
                {icon}
                <ThemedText style={styles.sectionTitle}>{title}</ThemedText>
            </View>
            <FlatList
                data={classes}
                renderItem={renderClassItem}
                keyExtractor={(item) => item.id}
                contentContainerStyle={styles.classesList}
                ListEmptyComponent={<ThemedText>No classes available</ThemedText>}
            />
        </ThemedView>
    );
    const renderFeedSectionHeader = (title: string, icon: React.ReactNode) => (
        <ThemedView style={styles.section}>
            <View style={styles.sectionHeader}>
                {icon}
                <ThemedText style={styles.sectionTitle}>{title}</ThemedText>
            </View>
            <FlatList
                data={feed}
                renderItem={renderFeedItem}
                keyExtractor={(item) => item.id}
                contentContainerStyle={styles.classesList}
                ListEmptyComponent={<ThemedText>No classes available</ThemedText>}
            />
        </ThemedView>
    );

    return (
        <SafeAreaView style={styles.container}>
            <GestureHandlerRootView style={styles.gestureRootView}>
                <FlatList
                    data={[]}
                    renderItem={() => null}
                    keyExtractor={() => "header-footer"}
                    ListHeaderComponent={() => (
                        <ThemedView style={styles.header}>
                            <Ionicons name="school-outline" size={24} color="tomato" />
                            <ThemedText style={styles.headerText}>Dashboard</ThemedText>
                        </ThemedView>
                    )}
                    ListFooterComponent={() => (
                        <>
                            {renderClassSectionHeader(
                                "Today's Classes",
                                <Ionicons name="calendar-outline" size={20} />
                            )}
                            {renderFeedSectionHeader(
                                "Don't Miss Out",
                                <Feathericons name="bell" size={20} />
                            )}
                        </>
                    )}
                    contentContainerStyle={styles.listContainer}
                />
            </GestureHandlerRootView>
        </SafeAreaView>
    );
};

export default DashboardPage;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
    gestureRootView: {
        flex: 1,
    },
    header: {
        flexDirection: 'row',
        alignItems: 'center',
        padding: 16,
        backgroundColor: '#f8f8f8',
    },
    headerText: {
        marginLeft: 8,
        fontSize: 20,
        fontWeight: 'bold',
    },
    section: {
        padding: 16,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
    },
    sectionHeader: {
        flexDirection: 'row',
        alignItems: 'center',
        marginBottom: 8,
    },
    sectionTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginLeft: 10,
    },
    classesList: {
        padding: 0,
    },
    listContainer: {
        paddingBottom: 16, // To ensure there's space at the bottom
    },
    classItem: {
        flexDirection: 'row',
        alignItems: 'center',
        padding: 16,
        borderBottomWidth: 1,
        borderBottomColor: '#eee',
    },
    icon: {
        marginRight: 16,
    },
    classInfo: {
        flex: 1,
    },
    className: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    classTime: {
        fontSize: 16,
        color: '#666',
    },
});
